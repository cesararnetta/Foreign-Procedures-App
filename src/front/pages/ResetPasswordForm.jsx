import { useState } from "react";
import { useNavigate, useSearchParams } from "react-router-dom"
import { authenticationServices } from "../services/authenticationServices";


export const ResetPasswordForm = () => {
    const navigate = useNavigate();
    const [searchParams] = useSearchParams();
    const token = searchParams.get("token");

    const [password, setPassword] = useState("");
    const [successMessage, setSuccessMessage] = useState("");
    const [errorMessage, setErrorMessage] = useState("");
    const [isSubmitting, setIsSubmitting] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsSubmitting(true);
        try {
            if (!token) {
                throw new Error("Token no obtenido");
            }
            await authenticationServices.resetPassword(password.trim(), token)
            setSuccessMessage("Restablecida contraseña con éxito ✅");
            setTimeout(() => {
                setSuccessMessage("");
                navigate("/login");
            }, 1500);
        } catch (error) {
            console.error('Error al iniciar sesión:', error);
            setErrorMessage("Error al restablecer contraseña ❌");
            setTimeout(() => setErrorMessage(""), 1500);
        } finally {
            setIsSubmitting(false);
        }
    };


    return (
        <form onSubmit={handleSubmit}>
            <div className="container d-flex align-items-center justify-content-center min-vh-100">
                <div className="card p-4 shadow-sm" style={{ maxWidth: "400px", width: "100%" }}>
                    <h3 className="text-center text-primary mb-2">Bienvenido</h3>
                    <p className="text-center text-muted mb-4">Inicia sesión para continuar</p>
                    {successMessage && (
                        <div className="alert alert-success text-center" role="alert">
                            {successMessage}
                        </div>
                    )}
                    {errorMessage && (
                        <div className="alert alert-danger text-center" role="alert">
                            {errorMessage}
                        </div>
                    )}

                    <div className="mb-3 text-center">
                        <label htmlFor="password" className="form-label">
                            <i className="fas fa-lock me-2 text-secondary"></i>
                            Nueva contraseña
                        </label>
                        <input
                            type="password"
                            className="form-control"
                            id="password"
                            name="password"
                            value={password}
                            onChange={e => setPassword(e.target.value)}
                            required
                            minLength={6}
                            disabled={isSubmitting}
                        />
                    </div>

                    <button type="submit" className="btn btn-primary w-100 mb-2" disabled={isSubmitting}>
                        {isSubmitting ? "Espera, restableciendo..." : "Restablecer contraseña"}
                    </button>

                </div>
            </div>
        </form>
    )
}

