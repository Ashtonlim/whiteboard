
def sortVids(videos, course):
    catVids = {}
    courseVids = [[] for _ in range(course.count())]
    for vid in videos:
        courseVids[vid.course.id - 1].append({
            "id" : vid.id,
            "courseID" : vid.course.id,
            "title" : vid.title,
            "desc" : vid.desc,
            "video" : vid.video.url,
            "thumbnail" : vid.thumbnail.url,
            "likes" : vid.likes,
            "dislikes" : vid.dislikes,
            "uploadDate" : vid.uploadDate,
        })
    for c in course:
        if len(courseVids[c.id-1]) != 0:
            vids = {i["id"]:i for i in courseVids[c.id-1] if i["courseID"] == c.id}
            catVids[str(c.id)] = {
                "courseName" : c.course,
                "courseCode" : c.courseCode,
                "ve" : vids
            }
    return catVids