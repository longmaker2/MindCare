document.addEventListener("DOMContentLoaded", function () {
  console.log("✅ JavaScript file loaded!");

  const contactForm = document.getElementById("contact-form");
  const submitButton = contactForm ? contactForm.querySelector("button") : null;
  const successPopup = document.getElementById("success-popup");

  if (!contactForm) {
      console.error("❌ Error: contact-form not found in HTML!");
      return;
  }

  if (!successPopup) {
      console.error("❌ Error: success-popup div is missing in the HTML!");
      return;
  }

  console.log("✅ Form and success-popup found!");

  let isSubmitting = false; // Prevent multiple submissions

  contactForm.addEventListener("submit", function (event) {
      event.preventDefault(); // Stop page reload

      if (isSubmitting) return;
      isSubmitting = true;
      submitButton.disabled = true; // Disable button during request

      let formData = new FormData(this);

      console.log("📡 Sending POST request...");

      fetch(this.action, {
          method: "POST",
          body: formData,
          headers: { "X-Requested-With": "XMLHttpRequest" }
      })
      .then(response => {
          console.log("✅ Received Response:", response);
          return response.json();
      })
      .then(data => {
          console.log("✅ Server Response:", data);

          if (data.message) {
              console.log("✅ Popup should appear now!");
              
              successPopup.innerText = data.message; // ✅ Set text
              successPopup.style.display = "block"; // ✅ Show popup
              
              setTimeout(() => {
                  successPopup.style.display = "none"; // ✅ Hide after 3 sec
                  contactForm.reset(); // ✅ Reset form
                  isSubmitting = false;
                  submitButton.disabled = false;
              }, 3000);
          } else {
              console.error("❌ Unexpected response:", data);
          }
      })
      .catch(error => {
          console.error("❌ Fetch Error:", error);
          alert("An error occurred. Please try again.");
          isSubmitting = false;
          submitButton.disabled = false;
      });
  });
});
  $(document).ready(function () {
    $(".appointment-form").off("submit").on("submit", function (event) {
        event.preventDefault(); // Prevent default form submission

        var formData = $(this).serialize(); // Serialize form data
        var professionalId = $(this).find("input[name='professional']").val(); // Get professional ID

        console.log("📢 Sending appointment request for Professional ID:", professionalId);

        // Get CSRF Token from the form
        var csrftoken = $("input[name=csrfmiddlewaretoken]").val();

        var submitBtn = $(this).find("button[type='submit']");
        if (submitBtn.prop("disabled")) {
            return;  // Prevent duplicate submission
        }

        submitBtn.prop("disabled", true).text("Booking..."); // Disable button to prevent multiple clicks

        $.ajax({
            type: "POST",
            url: $(this).attr("action"),
            data: formData,
            headers: { "X-CSRFToken": csrftoken }, // Ensure CSRF token is sent
            success: function (response) {
                console.log("✅ AJAX Response:", response);

                if (response.message) {
                    $("#success-popup").text(response.message).fadeIn().delay(3000).fadeOut();

                    var selectedSlot = $("select[name='time']").find("option:selected").val();

                    // ✅ Update the slot in the available list
                    $("ul").find("li:contains('" + selectedSlot + "')").html(
                        `<span style="color: red;">${selectedSlot} - Booked</span>`
                    );

                    // ✅ Disable the booked slot in the dropdown
                    $("select[name='time']").find("option:selected").prop("disabled", true).css("color", "red").text(selectedSlot + " - Booked");

                    // ✅ Clear form fields after submission
                    $(".appointment-form")[0].reset();

                    setTimeout(() => {
                        submitBtn.prop("disabled", false).text("Book Appointment");
                    }, 3000);
                } else {
                    console.error("❌ Unexpected response format:", response);
                }
            },
            error: function (xhr, status, error) {
                console.error("❌ Error booking appointment:", xhr.responseText);
                alert("Error booking appointment. Please try again.");
                submitBtn.prop("disabled", false).text("Book Appointment");
            }
        });
    });
});


document.addEventListener("DOMContentLoaded", function () {
    const contactForm = document.getElementById("contact-form");
    const successPopup = document.getElementById("success-popup");

    if (!contactForm) {
        console.error("❌ Error: contact-form not found in HTML!");
        return;
    }

    if (!successPopup) {
        console.error("❌ Error: success-popup div is missing in the HTML!");
        return;
    }

    contactForm.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent default form submission
        let formData = new FormData(this);

        fetch(this.action, {
            method: "POST",
            body: formData,
            headers: { "X-Requested-With": "XMLHttpRequest" }
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                console.log("✅ Popup should appear now!");
                successPopup.innerText = data.message;
                successPopup.style.display = "block";
                setTimeout(() => {
                    successPopup.style.display = "none";
                    contactForm.reset();
                }, 3000);
            } else {
                console.error("❌ Unexpected response:", data);
            }
        })
        .catch(error => {
            console.error("❌ Fetch Error:", error);
            alert("An error occurred. Please try again.");
        });
    });
});
    function saveLanguage(language) {
        localStorage.setItem("selectedLanguage", language);
        document.cookie = "language=" + language + ";path=/";
    }
    
    function getSavedLanguage() {
        let savedLang = localStorage.getItem("selectedLanguage");
        let cookieLang = document.cookie.split("; ").find(row => row.startsWith("language="));
        return savedLang || (cookieLang ? cookieLang.split("=")[1] : "en");
    }
    
    // ✅ Apply saved language on page load
    document.addEventListener("DOMContentLoaded", function () {
        let savedLanguage = getSavedLanguage();
        document.getElementById("language-selector").value = savedLanguage;
        translatePage(savedLanguage, true);
    });
    
    function getCSRFToken() {
        let csrfToken = document.cookie.split("; ").find(row => row.startsWith("csrftoken="));
        return csrfToken ? csrfToken.split("=")[1] : "";
    }

    function translatePage() {
    console.log("✅ Translate button clicked! Processing...");

    let selectedLanguage = document.getElementById("language-selector").value;
    let elements = document.querySelectorAll("[data-translate]");

    if (!selectedLanguage) {
        alert("Please select a language first!");
        return;
    }

    let texts = [];
    elements.forEach(element => texts.push(element.textContent.trim()));

    let textArray = texts.join("|"); // Convert array to a string

    console.log("🔵 Sending translation request:", { textArray, selectedLanguage });

    fetch("/translate/", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRFToken": getCSRFToken()
        },
        body: new URLSearchParams({
            "text": textArray,
            "language": selectedLanguage
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log("✅ Translation response:", data);

        if (data.translated_text) {
            let translatedTexts = data.translated_text.split("|");
            elements.forEach((element, index) => {
                element.textContent = translatedTexts[index] || element.textContent;
            });

            console.log("✅ Translation applied successfully:", translatedTexts);
        } else {
            console.error("❌ Translation error:", data.error);
            alert("Translation error: " + data.error);
        }
    })
    .catch(error => console.error("❌ Translation failed:", error));
}

document.addEventListener("DOMContentLoaded", function () {
    let today = new Date().toISOString().split("T")[0]; // Get today's date in YYYY-MM-DD format
    
    // ✅ Apply to ALL appointment forms on the page
    document.querySelectorAll(".appointment-form input[name='date']").forEach(function (dateInput) {
        dateInput.setAttribute("min", today);
    });
});