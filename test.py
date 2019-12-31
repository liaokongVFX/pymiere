import pymiere

get_sequence = """var sequence = app.project.activeSequence;
var all_tracks = [];
for(var i=0; i<sequence.videoTracks.numTracks; i++){
    all_tracks.push(sequence.videoTracks[i]);
}
JSON.stringify(all_tracks)"""

if __name__== "__main__":
    PYMIERE = pymiere.Pymiere()
    sequence_info = PYMIERE.eval_script("$._pymiere['myFirstId'] = app.project.activeSequence; JSON.stringify($._pymiere['myFirstId']);")
    sequence = pymiere.objects.Sequence('myFirstId', **sequence_info)
    print(sequence.name)
    print(sequence.id)
    sequence.name = "nom sympa"
    try:
        sequence.id = "caca"
    except AttributeError:
        print("Id is read only check ok")
    print(sequence.getInPoint())
    playerPos = sequence.getPlayerPosition()
    print(playerPos)
    print(playerPos.ticks)
    clip = sequence.videoTracks[0].clips[0]
    new_time = pymiere.objects.Time()
    new_time.seconds = 5
    sequence.setPlayerPosition(str(new_time.ticks))

    print(new_time.ticks)

    sequence.setOutPoint(10)