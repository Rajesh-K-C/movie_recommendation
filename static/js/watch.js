"use strict";
const csrfToken = document.querySelector("meta[name='csrf-token']").content;
async function likeBtn(e, id, url) {
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
                    e.lastElementChild.textContent = (Number.parseInt(e.lastElementChild.textContent || "") + 1).toString();
                }
                else {
                    e.lastElementChild.textContent = (Number.parseInt(e.lastElementChild.textContent || "") - 1).toString();
                }
            }
            else {
                alert(responseData.error);
            }
        }
        catch (error) { }
    }
}
const iframe = document.querySelector('iframe');
iframe.onload = async () => {
    let id = Number.parseInt(iframe.getAttribute("data-movie"));
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
    }
    catch (error) { }
};
async function addToMyList(e, id, url) {
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
                    e.lastElementChild.textContent = "✔️";
                }
                else {
                    e.lastElementChild.textContent = "➕";
                }
            }
            else {
                alert(responseData.error);
            }
        }
        catch (error) { }
    }
}
