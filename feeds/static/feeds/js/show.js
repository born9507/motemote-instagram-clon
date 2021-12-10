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
    const commentId = response.data.id;

    const commentList = document.getElementById('comment-list')
    commentList.innerHTML = commentList.innerHTML + `
      <p id="${commentId}-comment">
        ${response.data.content}
        <a id="${commentId}-comment-like-button" onClick="onClickCommentLikeButton(${feedId}, ${commentId})">
          0 Likes
        </a>
        <a onClick="onClickCommentDeleteButton(${feedId}, ${commentId})">댓글 삭제</a>
        <a href="/feeds/${feedId}/comments/${response.data.id.toString()}/create/">대댓글 달기</a>
      </p>
    `

    document.getElementById('comment-input').value = '';
  }
}

const onClickLikeButton = async (feedId) => {
  const feedLikeButton = document.getElementById(`${feedId}-like-button`);
  const response = await axios.get(`/feeds/${feedId}/like/`);
  feedLikeButton.innerHTML = `${response.data.feedLikeCount} Likes`
}

const onClickCommentLikeButton = async (feedId, commentId) => {
  const commentLikeButton = document.getElementById(`${commentId}-comment-like-button`);
  const response = await axios.get(`/feeds/${feedId}/comments/${commentId}/like/`);
  commentLikeButton.innerHTML = `${response.data.commentLikeCount} Likes`
}

const onClickCommentDeleteButton = async (feedId, commentId) => {
  const response = await axios.get(`/feeds/${feedId}/comments/${commentId}/delete/`);
  const commentDeleted = document.getElementById(`${response.data.id}-comment`);
  commentDeleted.remove();
}
