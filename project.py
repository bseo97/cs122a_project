import sys
from create_tables import create_tables
from import_data import import_csv_data
from insert_viewer import insert_viewer
from add_genre import add_genre
from delete_viewer import delete_viewer
from insert_movie import insert_movie
from insert_session import insert_session
from update_release import update_release
from get_releases import get_releases
from popular_release import popular_release
from title_release import title_release
from active_viewers import active_viewers
from videos_viewed import videos_viewed

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("NO COMMAND PASSED")
    elif sys.argv[1] == "import" and len(sys.argv) == 3:
        create_tables()
        if(import_csv_data(sys.argv[2])):
            print("Success")
        else:
            print("Fail")
    elif sys.argv[1] == "insertViewer" and len(sys.argv) == 14:
        create_tables()
        if(insert_viewer(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10], sys.argv[11], sys.argv[12], sys.argv[13])):
            print("Success")
        else:
            print("Fail")
    elif sys.argv[1] == "addGenre" and len(sys.argv) == 4:
        if(add_genre(sys.argv[2],sys.argv[3])):
            print("Success")
        else:
            print("Fail")
    elif sys.argv[1] == "deleteViewer" and len(sys.argv) == 3:
        if(delete_viewer(sys.argv[2])):
            print("Success")
        else:
            print("Fail")
    elif sys.argv[1] == "insertMovie" and len(sys.argv) == 4:
        if(insert_movie(sys.argv[2], sys.argv[3])):
            print("Success")
        else:
            print("Fail")
    elif sys.argv[1] == "insertSession" and len(sys.argv) == 10:
        if(insert_session(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8],sys.argv[9])):
            print("Success")
        else:
            print("Fail")
    elif sys.argv[1] == "updateRelease" and len(sys.argv) == 4:
        if(update_release(sys.argv[2],sys.argv[3])):
            print("Success")
        else:
            print("Fail")
    elif sys.argv[1] == "listReleases" and len(sys.argv) == 3:
        #Can change for a better way to join tuples if you want
        for values in get_releases[sys.argv[2]]:
            #Join the tuple into a string to print. Use format rid,genre,title
            printString = ""
            for value in values:
                printString += (str(value) + ",")
            #Splice the string so that the last comma is not included
            print(printString[:len(printString) - 1])
    elif sys.argv[1] == "popularRelease" and len(sys.argv) == 3:
        results = popular_release(int(sys.argv[2]))
        for values in results:
            print(",".join(map(str, values)))  # Output in CSV format

    elif sys.argv[1] == "releaseTitle" and len(sys.argv) == 3:
        results = title_release(int(sys.argv[2]))
        for values in results:
            print(",".join(map(str, values)))  # Output in CSV format

    elif sys.argv[1] == "activeViewer" and len(sys.argv) == 5:
        results = active_viewers(int(sys.argv[2]), sys.argv[3], sys.argv[4])
        for values in results:
            print(",".join(map(str, values)))  # Output in CSV format

    elif sys.argv[1] == "videosViewed" and len(sys.argv) == 3:
        results = videos_viewed(int(sys.argv[2]))
        for values in results:
            print(",".join(map(str, values)))  # Output in CSV format

    else:
         print("Invalid Input")

