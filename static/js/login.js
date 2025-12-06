document.getElementById("login").addEventListener("click", () => {
    const email = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();

    if (email === "") {
        toastr.error("Email can't be blank");
        return;
    }
    if(!validateEmail(email)){
        toastr.error("Please enter valid email.")
        return;
    }
    if (password === "") {
        toastr.error("Password can't be blank");
        return;
    }

    fetch('/login', {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email: email, password: password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            toastr.success(data.message);
            window.location.href = data.redirect_url;
        } else {
            toastr.error(data.message);
        }
    })
    .catch(error => {
        console.error("Error:", error);
        toastr.error("An error occurred. Please try again.");
    });
});
