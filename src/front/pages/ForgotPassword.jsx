import { useState } from "react";
import { authenticationServices } from "../services/authenticationServices";

export const ForgotPassword = () => {
  const [email, setEmail] = useState("");
  const [successMessage, setSuccessMessage] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    setErrorMessage("");
    setSuccessMessage("");

    try {
      if (!email.trim()) throw new Error("El correo es requerido");

      await authenticationServices.forgotPassword({ email: email.trim() });
      setSuccessMessage("Correo enviado con instrucciones para restablecer la contraseña ✅");
    } catch (error) {
      setErrorMessage("No se pudo enviar el correo. Intenta de nuevo ❌");
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="container d-flex align-items-center justify-content-center min-vh-100">
        <div className="card p-4 shadow-sm" style={{ maxWidth: "400px", width: "100%" }}>
          <h3 className="text-center text-primary mb-2">¿Olvidaste tu contraseña?</h3>
          <p className="text-center text-muted mb-4">Ingresa tu correo para recibir instrucciones</p>

          {successMessage && (
            <div className="alert alert-success text-center">{successMessage}</div>
          )}
          {errorMessage && (
            <div className="alert alert-danger text-center">{errorMessage}</div>
          )}

          <div className="mb-3 text-center">
            <label htmlFor="email" className="form-label">
              <i className="fas fa-envelope me-2 text-secondary"></i> Correo electrónico
            </label>
            <input
              type="email"
              className="form-control"
              id="email"
              name="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              disabled={isSubmitting}
            />
          </div>

          <button type="submit" className="btn btn-primary w-100" disabled={isSubmitting}>
            {isSubmitting ? "Enviando correo..." : "Enviar instrucciones a tu correo"}
          </button>
        </div>
      </div>
    </form>
  );
};