function initAutocomplete() {
  const searchInput = document.getElementById("search");
  const suggestionsContainer = document.getElementById("suggestions");

  if (!searchInput) return;

  let timeoutId;

  searchInput.addEventListener("input", function () {
    const query = this.value.trim();

    clearTimeout(timeoutId);

    suggestionsContainer.innerHTML = "";
    suggestionsContainer.style.display = "none";

    if (query.length < 2) {
      return;
    }

    timeoutId = setTimeout(() => {
      fetch(`/autocomplete/?q=${encodeURIComponent(query)}`)
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json();
        })
        .then((books) => {
          suggestionsContainer.innerHTML = "";

          if (books.length > 0) {
            books.forEach((book) => {
              const div = document.createElement("div");
              div.className = "suggestion-item";

              let displayText = book.title;
              if (book.author) {
                displayText += `, ${book.author}`;
              }

              div.innerHTML = `<div class="suggestion-full">${displayText}</div>`;

              div.addEventListener("click", function () {
                searchInput.value = book.title;
                suggestionsContainer.style.display = "none";
              });

              suggestionsContainer.appendChild(div);
            });
            suggestionsContainer.style.display = "block";
          }
        })
        .catch((error) => {
          console.error("Error fetching autocomplete:", error);
        });
    }, 300);
  });

  document.addEventListener("click", function (e) {
    if (
      !searchInput.contains(e.target) &&
      !suggestionsContainer.contains(e.target)
    ) {
      suggestionsContainer.style.display = "none";
    }
  });

  searchInput.addEventListener("keydown", function (e) {
    const items = suggestionsContainer.querySelectorAll(".suggestion-item");
    let activeItem = suggestionsContainer.querySelector(
      ".suggestion-item.active"
    );

    if (e.key === "ArrowDown") {
      e.preventDefault();
      if (items.length === 0) return;

      if (!activeItem) {
        items[0].classList.add("active");
      } else {
        activeItem.classList.remove("active");
        const next = activeItem.nextElementSibling || items[0];
        next.classList.add("active");
      }
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      if (items.length === 0) return;

      if (activeItem) {
        activeItem.classList.remove("active");
        const prev =
          activeItem.previousElementSibling || items[items.length - 1];
        prev.classList.add("active");
      }
    } else if (e.key === "Enter" && activeItem) {
      e.preventDefault();
      activeItem.click();
    } else if (e.key === "Escape") {
      suggestionsContainer.style.display = "none";
    }
  });
}

document.addEventListener("DOMContentLoaded", initAutocomplete);
