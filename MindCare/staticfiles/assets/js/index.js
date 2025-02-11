document.addEventListener("DOMContentLoaded", function () {
  const contactForm = document.getElementById("contact-form");
  const submitButton = contactForm.querySelector("button");
  const successPopup = document.getElementById("success-popup");

  if (!successPopup) {
      console.error("❌ Error: success-popup div is missing in the HTML!");
      return;
  }

  let isSubmitting = false; // Prevent multiple submissions

  contactForm.addEventListener("submit", function (event) {
      event.preventDefault(); // Stop page reload

      if (isSubmitting) return;
      isSubmitting = true;
      submitButton.disabled = true; // Disable button during request

      let formData = new FormData(this);

      fetch(this.action, {
          method: "POST",
          body: formData,
          headers: { "X-Requested-With": "XMLHttpRequest" }
      })
      .then(response => response.json())  // Ensure JSON response
      .then(data => {
          console.log("Server Response:", data);  // Debugging

          if (data.message) {
              console.log("Popup should appear now!");

              successPopup.innerText = data.message; // ✅ Set text
              successPopup.style.display = "block"; // ✅ Show popup
              
              setTimeout(() => {
                  successPopup.style.display = "none"; // ✅ Hide after 3 sec
                  contactForm.reset(); // ✅ Reset form
                  isSubmitting = false;
                  submitButton.disabled = false;
              }, 3000);
          } else {
              console.error("Unexpected response:", data);
          }
      })
      .catch(error => {
          console.error("Error:", error);
          isSubmitting = false;
          submitButton.disabled = false;
      });
  });
});
