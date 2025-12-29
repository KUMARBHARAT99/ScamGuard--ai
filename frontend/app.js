function go(id) {
  document.getElementById(id).scrollIntoView({ behavior: "smooth" });
}

function resetAll() {
  document.getElementById("messageInput").value = "";
  document.getElementById("result").classList.add("hidden");
}

async function analyzeMessage() {
  const msg = document.getElementById("messageInput").value;
  if (!msg.trim()) {
    alert("Please enter a message");
    return;
  }

  document.getElementById("loader").classList.remove("hidden");
  document.getElementById("result").classList.add("hidden");

  try {
    const res = await fetch("http://127.0.0.1:8000/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: msg, use_llm: true })
    });

    const data = await res.json();

    document.getElementById("ruleResult").innerText = data.rule_based;

    // ===== LLM UI SPLIT =====
    const llmText = data.llm;
    const container = document.getElementById("llmCards");
    container.innerHTML = "";

    const sections = {
      scam: /Scam Type:(.*)/i,
      risk: /Risk Level:(.*)/i,
      explanation: /Explanation:(.*?)(Safe Action Advice:|$)/is,
      safe: /Safe Action Advice:(.*)/is
    };

    if (sections.scam.test(llmText)) {
      container.innerHTML += `
        <div class="llm-card card-scam">
          <h4>🚨 Scam Type</h4>
          <p>${llmText.match(sections.scam)[1]}</p>
        </div>`;
    }

    if (sections.risk.test(llmText)) {
      container.innerHTML += `
        <div class="llm-card card-risk">
          <h4>⚠ Risk Level</h4>
          <p>${llmText.match(sections.risk)[1]}</p>
        </div>`;
    }

    if (sections.explanation.test(llmText)) {
      container.innerHTML += `
        <div class="llm-card card-explain">
          <h4>ℹ Why This Is a Scam</h4>
          <p>${llmText.match(sections.explanation)[1]}</p>
        </div>`;
    }

    if (sections.safe.test(llmText)) {
      const points = llmText
        .match(sections.safe)[1]
        .split("*")
        .filter(p => p.trim());

      container.innerHTML += `
        <div class="llm-card card-safe">
          <h4>✅ What You Should Do</h4>
          <ul>${points.map(p => `<li>${p}</li>`).join("")}</ul>
        </div>`;
    }

    document.getElementById("result").classList.remove("hidden");
  }
  catch (e) {
    alert("Backend or LLM error");
  }
  finally {
    document.getElementById("loader").classList.add("hidden");
  }
}


function openSettings() {
  document.getElementById("settingsModal").classList.add("active");
}

function closeSettings() {
  document.getElementById("settingsModal").classList.remove("active");
}

function go(id) {
  closeSettings(); // safety
  document.getElementById(id).scrollIntoView({ behavior: "smooth" });
}

