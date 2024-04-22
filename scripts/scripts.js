function example() {
  fetch("http://127.0.0.1:5000/example")
    .then((response) => response.json())
    .then((data) => {
      if (typeof data == "string") alert(data);
      else {
        let inputField = document.getElementById("inputField");
        let input = document.createElement("p");
        let content = JSON.stringify(data["Content"], null, "\t");
        console.log(content);
        input.className = "input";
        input.textContent = content;
        inputField.appendChild(input);

        for (let i = 0; i < data["ResourceStatus"].length; i++) {
          let outputMessage = document.getElementById("outputMessage");
          let output = document.createElement("p");
          let resourceStatus = data["ResourceStatus"][i];
          output.className = "output";
          output.textContent =
            "Statement " + i + " - Resource Status: " + resourceStatus;
          if (resourceStatus == false) output.style.color = "red";
          else output.style.color = "rgb(8, 188, 8)";
          outputMessage.appendChild(output);
        }
      }
    });
}

document
  .getElementById("uploadForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the default form submission

    // Get the file input element
    const fileInput = document.getElementById("myFile");

    // Check if a file is selected
    if (fileInput.files.length === 0) {
      alert("Please select a file.");
      return;
    }

    // Get the selected file
    const file = fileInput.files[0];

    // Check if the selected file is of JSON type
    if (!file.type.match(".json")) {
      alert("Please select a JSON file.");
      return;
    }

    // REQUEST
    // Create a FormData object
    const formData = new FormData();

    // Append the file to FormData
    formData.append("file", file);

    // Send the AJAX request
    fetch("http://127.0.0.1:5000/verify", {
      method: "POST",
      body: formData,
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        if (typeof data == "string") alert(data);
        else {
          let inputField = document.getElementById("inputField");

          // Remove old result
          let old_input = document.getElementsByClassName("input");
          old_input[0].remove();

          let input = document.createElement("p");
          let content = JSON.stringify(data["Content"], null, "\t");
          input.className = "input";
          input.textContent = content;
          inputField.appendChild(input);

          // Remove old result
          let old_output = document.getElementsByClassName("output");
          while (old_output[0]) {
            old_output[0].remove();
          }

          for (let i = 0; i < data["ResourceStatus"].length; i++) {
            let outputMessage = document.getElementById("outputMessage");
            let output = document.createElement("p");
            let resourceStatus = data["ResourceStatus"][i];
            output.className = "output";
            output.textContent =
              "Statement " + i + " - Resource Status: " + resourceStatus;
            if (resourceStatus == false) output.style.color = "red";
            else output.style.color = "rgb(8, 188, 8)";
            outputMessage.appendChild(output);
          }
        }
      })
      .catch((error) => {
        // Handle error response
        console.error("Error:", error.message);
        alert("An error occurred, please try again later.");
      });
  });
