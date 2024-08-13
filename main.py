import discord
from discord.ext import commands, tasks
from discord import app_commands
import datetime

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

ALLOWED_ROLE_ID = 726489827905896500
ATIS_INFO = {}
ATIS_TASK = None

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="setatis")
@app_commands.describe(
    airport="Airport code",
    atis_letter="ATIS letter (one letter only, no numbers)",
    winds="Current winds at the airport",
    trans_level="Transition level",
    visibility="Visibility",
    active_rwy="Active runway"
)
async def setatis(interaction: discord.Interaction, airport: str, atis_letter: str, winds: str, trans_level: str, 
                  visibility: str, active_rwy: str):
    if not has_required_role(interaction.user):
        await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)
        return

    if len(atis_letter) != 1 or not atis_letter.isalpha():
        await interaction.response.send_message("ATIS letter must be a single alphabetic character.", ephemeral=True)
        return

    ATIS_INFO[interaction.channel_id] = {
        'airport': airport,
        'atis_letter': atis_letter.upper(),
        'winds': winds,
        'trans_level': trans_level,
        'visibility': visibility,
        'active_rwy': active_rwy,
        'channel': interaction.channel
    }

    await interaction.response.send_message("ATIS information set. Starting broadcast.", ephemeral=True)
    
    global ATIS_TASK
    if ATIS_TASK is None or ATIS_TASK.is_running() is False:
        ATIS_TASK = broadcast_atis.start()
    else:
        ATIS_TASK.restart()

@bot.tree.command(name="stopatis")
async def stopatis(interaction: discord.Interaction):
    if not has_required_role(interaction.user):
        await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)
        return

    if interaction.channel_id in ATIS_INFO:
        del ATIS_INFO[interaction.channel_id]
        await interaction.response.send_message("ATIS broadcast stopped for this channel.", ephemeral=True)
    else:
        await interaction.response.send_message("No active ATIS broadcast in this channel.", ephemeral=True)

    if len(ATIS_INFO) == 0 and ATIS_TASK is not None:
        ATIS_TASK.cancel()

@bot.tree.command(name="changeatis")
@app_commands.describe(
    airport="Airport code",
    atis_letter="ATIS letter (one letter only, no numbers)",
    winds="Current winds at the airport",
    trans_level="Transition level",
    visibility="Visibility",
    active_rwy="Active runway"
)
async def changeatis(interaction: discord.Interaction, airport: str = None, atis_letter: str = None, winds: str = None,
                     trans_level: str = None, visibility: str = None, active_rwy: str = None):
    if not has_required_role(interaction.user):
        await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)
        return

    if interaction.channel_id not in ATIS_INFO:
        await interaction.response.send_message("No active ATIS broadcast in this channel. Use /setatis to start a new one.", ephemeral=True)
        return

    if atis_letter is not None:
        if len(atis_letter) != 1 or not atis_letter.isalpha():
            await interaction.response.send_message("ATIS letter must be a single alphabetic character.", ephemeral=True)
            return
        ATIS_INFO[interaction.channel_id]['atis_letter'] = atis_letter.upper()

    update_fields = ['airport', 'winds', 'trans_level', 'visibility', 'active_rwy']
    for field in update_fields:
        if locals()[field] is not None:
            ATIS_INFO[interaction.channel_id][field] = locals()[field]

    await interaction.response.send_message("ATIS information updated.", ephemeral=True)  

def has_required_role(user):
    return discord.utils.get(user.roles, id=ALLOWED_ROLE_ID) is not None

@tasks.loop(minutes=10)
async def broadcast_atis():
    for channel_id, info in ATIS_INFO.items():
        embed = create_atis_embed(info)
        await info['channel'].send(embed=embed)

def create_atis_embed(info):
    current_time = datetime.datetime.now(datetime.timezone.utc).strftime("%H%MZ")
    
    atis_template = f"""{info['airport']} ATIS INFO {info['atis_letter']}. {current_time}. Winds at {info['winds']} Trans Level ({info['trans_level']}). Visibility is {info['visibility']} RWY {info['active_rwy']}, IN USE. EXP ILS APCH RWY {info['active_rwy']}, OR VIS APCH RWY {info['active_rwy']}......ADVS YOU HAVE INFO {info['atis_letter']}."""
    
    embed = discord.Embed(
        title=f"ATIS {info['airport']} {info['atis_letter']}",
        description=atis_template,
        color=discord.Color.orange()
    )
    
    return embed

bot.run('botid')