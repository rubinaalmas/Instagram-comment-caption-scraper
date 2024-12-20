
import instaloader
import csv
import time

def get_ig_comments(post_url, username):
    L = instaloader.Instaloader()
    L.load_session_from_file(username, f"/Users/rubinaalmas/.config/instaloader/session-{username}")
    shortcode = post_url.split("/")[-2]

    post = instaloader.Post.from_shortcode(L.context, shortcode)

    # Fetch the post caption
    caption = post.caption if post.caption else "No caption"
 
    comments_data = []
    for count, comment in enumerate(post.get_comments()):
        comments_data.append((comment.owner.username, comment.text,caption))
        
        #pausing for every 100 comments
        if (count + 1) % 100 == 0:
            time.sleep(60)  

    return comments_data


post_url = "your post url"
username = "your instagram username"

comments_data = get_ig_comments(post_url, username)

with open("comments.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Caption","Username", "Comment"]) 
    for caption, user, comment in comments_data:
        writer.writerow([caption, user, comment])

print("Comments saved to comments.csv")

