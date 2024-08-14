from cookiebot import CookieAPI

app = CookieAPI()
USER_ID = 887307645529231431
GUILD_ID = 1010915072694046794

async with app as con:
    user_stats = con.get_user_stats(USER_ID)
    member_stats = con.get_member_stats(USER_ID, GUILD_ID)
    member_activity = con.get_member_activity(USER_ID, GUILD_ID)

    print("User Stats")
    print("")
    print("Kekse: " + str(user_stats.cookies))
    print("Streak: " + str(user_stats.streak))
    print("Gearbeitet: " + str(user_stats.total_shifts))
    print("")
    print("Codingkeks")
    print("")
    print("Level: " + str(member_stats.level))
    print("Nachrichten: " + str(member_stats.msg_count))
    print("Xp: " + str(member_stats.xp))
    print("Rank: " + str(member_stats.msg_rank) + "/" + str(member_stats.msg_total_members))
    print("Voice: " + str(member_stats.voice_min) + " Minuten, " + str(round(member_stats.voice_min / 60)) + " Stunden")
    print("Voice Level: " + str(member_stats.voice_level))
    print("Voice Rank: " + str(member_stats.voice_rank) + "/" + str(member_stats.voice_total_members))
    print("Level Progress: " + str(member_stats.current_level_progress) + "/" + str(member_stats.current_level_end))
    print("")
    print("Letzte 14 Tage")
    print("")
    print("Nachrichten: " + str(member_activity.msg_count))
    print("Rank: " + str(member_activity.msg_rank))
    print("Voice: " + str(member_activity.voice_min) + " Minuten, " + str(round(member_activity.voice_min / 60)) + " Stunden")
    print("Voice Rank: " + str(member_activity.voice_rank))
    input("Drücke eine beliebige Taste um das Programm zu beenden...")