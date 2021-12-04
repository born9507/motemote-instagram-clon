axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

const onAddComment = async (feedId) => {
  const commentInputElement = document.getElementById("comment-input");
  console.log(commentInputElement.value);

  if (commentInputElement.value) {
    let data = new FormData();
    data.append("content", commentInputElement.value);
    // {"content": commentInputElement.value}

    const response = await axios.post(`/feeds/${feedId}/comments/`, data)

    const commentList = document.getElementById('comment-list')
    commentList.innerHTML = commentList.innerHTML + `
      <p>
        ${response.data.content}
        <a href="/feeds/${feedId}/comments/${response.data.id}}/like/">
          0 Likes
        </a>
        <a href="/feeds/${feedId}/comments/${response.data.id.toString()}}/delete/">댓글 삭제</a>
        <a href="/feeds/${feedId}/comments/${response.data.id.toString()}}/create/">대댓글 달기</a>
      </p>
    `
  }
}

/* <p>
  {{ comment.content }}
    <a href="/feeds/{{feed.id}}/comments/{{comment.id}}/like/?next={{request.path}}">
      {{ comment.like_users.count }} Likes
    </a>
    <a href="/feeds/{{feed.id}}/comments/{{comment.id}}/delete/">댓글 삭제</a>
    <a href="/feeds/{{feed.id}}/comments/{{comment.id}}/create/">대댓글 달기</a>
  {% endif %}
</p> */
