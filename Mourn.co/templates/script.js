function delayedPopup() {
    setTimeout(function() {
      displayPopup();
    }, 5000); // 5000 milliseconds = 5 seconds
  }
  
  // Function to display the pop-up
  function displayPopup() {
    var popup = document.getElementById('discountPopup');
    popup.style.display = 'block';
  }
  
  // Function to close the pop-up
  function closePopup() {
    var popup = document.getElementById('discountPopup');
    popup.style.display = 'none';
  }
  
  // Function to handle form submission
  function submitForm(event) {
    event.preventDefault(); // Prevent form from submitting normally
  
    // Get the phone number from the form
    var phoneNumber = document.getElementById('phoneNumber').value.trim();
  
    // Placeholder function to simulate sending SMS
    sendSMS(phoneNumber);
  }
  
  // Placeholder function to simulate sending SMS (replace with actual API call)
  function sendSMS(phoneNumber) {
    // Replace with your actual SMS service API integration code
    console.log("Sending SMS to: " + phoneNumber);
  
    // Example: Using setTimeout to simulate async operation (replace with actual async code)
    setTimeout(function() {
      alert("SMS sent successfully!");
      closePopup(); // Close the popup after successful submission (demo purpose)
    }, 2000); // Simulate 2 seconds delay
  }
  
  // Display the popup after delay on page load
  window.onload = function() {
    delayedPopup();
  };