const csrfToken = (document.querySelector("meta[name='csrf-token']") as HTMLMetaElement).content;

async function likeBtn(e: HTMLButtonElement, id: number, url: string) {
    if (e.lastElementChild) {
        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ id })
            });
            const responseData = await response.json();
            if (response.status == 200) {
                if (responseData.status) {
                    e.lastElementChild.textContent = "Liked"
                } else {
                    e.lastElementChild.textContent = "Like"
                }
            }else{
                alert(responseData.error);
            }

        } catch (error) { }
    }
}