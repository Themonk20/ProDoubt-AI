const submitButton = document.getElementById("submit-button");
const userInput = document.getElementById("user-input");
const responseText = document.getElementById("response-text");

submitButton.addEventListener("click", () => {

    const question = userInput.value.trim();

    if (question === "") {
        responseText.textContent = "Please enter a question.";
        return;
    }

    responseText.textContent = "Thinking...";

    chrome.tabs.query(
        {
            active: true,
            currentWindow: true
        },
        (tabs) => {

            chrome.tabs.sendMessage(
                tabs[0].id,
                {
                    type: "GET_PAGE_TEXT"
                },
                (response) => {

                    if (chrome.runtime.lastError) {
                        responseText.textContent = "Could not access this page.";
                        console.error(chrome.runtime.lastError);
                        return;
                    }

                    if (!response || !response.text) {
                        responseText.textContent = "No page content found.";
                        return;
                    }

                    fetch("http://127.0.0.1:8000/ask", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            question: question,
                            webpage: response.text
                        })
                    })
                    .then((res) => {

                        if (!res.ok) {
                            throw new Error("Backend request failed.");
                        }

                        return res.json();
                    })
                    .then((data) => {
                        responseText.textContent = data.answer;
                    })
                    .catch((error) => {
                        console.error(error);
                        responseText.textContent = "Error connecting to backend.";
                    });

                }
            );

        }
    );

});