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
            if (response.status == 200 && e.lastElementChild) {
                e.classList.toggle("text-blue-700");
                if (responseData.status) {
                    e.lastElementChild.textContent = (Number.parseInt(e.lastElementChild.textContent || "0") + 1).toString();
                } else {
                    e.lastElementChild.textContent = (Number.parseInt(e.lastElementChild.textContent || "0") - 1).toString();
                }
            } else {
                alert(responseData.error);
            }

        } catch (error) { }
    }
}

async function updateHistory(id: number) {
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
        return responseData.status;
    } catch (error) {
        return false;
    }
}

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