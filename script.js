// Listen for a click event on the generate button
document.getElementById("generate-button").addEventListener("click", async () => {
    // Get the input value for fashion style from the user
    const style = document.getElementById("style-input").value;

    try {
        // Make a POST request to the Flask server with the inputted style
        const response = await fetch("http://127.0.0.1:5000/generate-design", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ style: style })  // Send the style in the request body
        });

        // Check if the response is OK (status code 200)
        if (response.ok) {
            const data = await response.json();  // Parse the response JSON
            
            // Get the URL of the generated design image from the response
            const imageUrl = "data.images/MEN-Denim-id_00000089-01_7_additional_densepose.png";
            
            // Update the image source on the webpage with the generated image URL
            document.getElementById("design-preview").src = "images/MEN-Denim-id_00000089-01_7_additional_densepose.png";
        } else {
            // If the server response is not OK, show an error message
            console.error("Error generating design:", response.statusText);
        }
    } catch (error) {
        // Catch any errors and log them
        console.error("Error loading design:", error);
    }
});
