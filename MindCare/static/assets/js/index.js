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
