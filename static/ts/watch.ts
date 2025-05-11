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
            } else {
                alert(responseData.error);
            }

        } catch (error) { }
    }
}

const iframe = document.querySelector('iframe') as HTMLIFrameElement;
iframe.onload = async () => {
    let id: number = Number.parseInt(iframe.getAttribute("data-movie") as string);
    try {
        const response = await fetch("/movies/update-history/", {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id })
        });
        const responseData = await response.json();
        console.log(responseData);
    } catch (error) { }
};

async function addToMyList(e: HTMLButtonElement, id: number, url: string) {
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
                    e.lastElementChild.textContent = "✔️"
                } else {
                    e.lastElementChild.textContent = "➕"
                }
            } else {
                alert(responseData.error);
            }

        } catch (error) { }
    }
}