document.addEventListener("DOMContentLoaded", function () {

    const passwordInput = document.getElementById("password");
    const rulesBox = document.getElementById("password-rules");

    const lengthRule = document.getElementById("length");
    const lowerRule = document.getElementById("lower");
    const upperRule = document.getElementById("upper");
    const numberRule = document.getElementById("number");
    const specialRule = document.getElementById("special");

    const cpfInput = document.getElementById("cpf");

    if (cpfInput) {
        cpfInput.addEventListener("input", function () {
            this.value = this.value.replace(/\D/g, '');
        });
    }

    if (passwordInput) {

        passwordInput.addEventListener("focus", function () {
            if (rulesBox) {
                rulesBox.style.display = "block";
            }
        });

        passwordInput.addEventListener("blur", function () {
            if (rulesBox) {
                rulesBox.style.display = "none";
            }
        });

        passwordInput.addEventListener("input", function () {
            const value = this.value;

            if (lengthRule) {
                lengthRule.style.color = value.length >= 8 ? "green" : "red";
            }

            if (lowerRule) {
                lowerRule.style.color = /[a-z]/.test(value) ? "green" : "red";
            }

            if (upperRule) {
                upperRule.style.color = /[A-Z]/.test(value) ? "green" : "red";
            }

            if (numberRule) {
                numberRule.style.color = /\d/.test(value) ? "green" : "red";
            }

            if (specialRule) {
                specialRule.style.color = /[!@#$%^&*(),.?":{}|<>]/.test(value) ? "green" : "red";
            }
        });
    }

});