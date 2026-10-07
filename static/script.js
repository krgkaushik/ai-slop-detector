const textInput = document.getElementById("textInput");
const detectBtn = document.getElementById("detectBtn");
const clearBtn = document.getElementById("clearBtn");

const charCount = document.getElementById("charCount");
const loading = document.getElementById("loading");
const result = document.getElementById("result");

const predictionText = document.getElementById("predictionText");
const mainScore = document.getElementById("mainScore");

const aiScore = document.getElementById("aiScore");
const humanScore = document.getElementById("humanScore");

const aiBar = document.getElementById("aiBar");
const humanBar = document.getElementById("humanBar");

textInput.addEventListener("input", () => {
    charCount.textContent = `${textInput.value.length} characters`;
});

clearBtn.addEventListener("click", () => {
    textInput.value = "";
    charCount.textContent = "0 characters";
    result.classList.add("hidden");
});

detectBtn.addEventListener("click", async () => {

    const text = textInput.value.trim();

    if (!text) {
        alert("Please enter some text.");
        return;
    }

    detectBtn.disabled = true;
    loading.classList.remove("hidden");
    result.classList.add("hidden");

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: text })
        });

        if (!response.ok) {
            throw new Error("Prediction failed");
        }

        const data = await response.json();

        predictionText.textContent = data.prediction;

        mainScore.textContent = `${data.ai}%`;

        aiScore.textContent = `${data.ai}%`;
        humanScore.textContent = `${data.human}%`;

        aiBar.style.width = `${data.ai}%`;
        humanBar.style.width = `${data.human}%`;

        result.classList.remove("hidden");

    } catch (error) {
        alert("Unable to analyze the text. Please try again.");
    }

    loading.classList.add("hidden");
    detectBtn.disabled = false;
});