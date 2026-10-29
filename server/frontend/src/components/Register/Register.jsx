import React, { useState } from 'react';

const Register = ({ setShowModal, fetchUser }) => {
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [err, setErr] = useState("");

  const register = async () => {
    const register_url = `${window.location.origin}/djangoapp/register/`;

    const response = await fetch(register_url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        userName: userName,
        password: password,
        firstName: firstName,
        lastName: lastName,
        email: email,
      }),
    });

    const json = await response.json();

    if (json.status === "Authenticated") {
      sessionStorage.setItem('username', json.userName);
      if (typeof fetchUser === 'function') fetchUser();
      if (typeof setShowModal === 'function') setShowModal(false);
    } else if (json.error === "Already Registered") {
      setErr("This username is already taken. Please try a different one.");
    } else {
      setErr("Registration failed. Please try again.");
    }
  };

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-6">
          <div className="card shadow-lg">
            <div className="card-header bg-primary text-white text-center py-3">
              <h4 className="mb-0 fw-bold">
                <i className="fas fa-user-plus me-2"></i>Create Account
              </h4>
              <p className="mb-0 small">Join Best Cars Dealership</p>
            </div>
            <div className="card-body p-4">
              {err && (
                <div className="alert alert-danger" role="alert">
                  <i className="fas fa-exclamation-triangle me-2"></i>{err}
                </div>
              )}

              {/* Username Field */}
              <div className="mb-3">
                <label htmlFor="username" className="form-label fw-semibold">
                  <i className="fas fa-user me-1"></i> Username
                </label>
                <input
                  id="username"
                  type="text"
                  className="form-control"
                  placeholder="Enter your username"
                  value={userName}
                  onChange={(e) => setUserName(e.target.value)}
                  required
                />
              </div>

              {/* First Name Field */}
              <div className="mb-3">
                <label htmlFor="firstName" className="form-label fw-semibold">
                  <i className="fas fa-id-card me-1"></i> First Name
                </label>
                <input
                  id="firstName"
                  type="text"
                  className="form-control"
                  placeholder="Enter your first name"
                  value={firstName}
                  onChange={(e) => setFirstName(e.target.value)}
                  required
                />
              </div>

              {/* Last Name Field */}
              <div className="mb-3">
                <label htmlFor="lastName" className="form-label fw-semibold">
                  <i className="fas fa-id-card me-1"></i> Last Name
                </label>
                <input
                  id="lastName"
                  type="text"
                  className="form-control"
                  placeholder="Enter your last name"
                  value={lastName}
                  onChange={(e) => setLastName(e.target.value)}
                  required
                />
              </div>

              {/* Email Field */}
              <div className="mb-3">
                <label htmlFor="email" className="form-label fw-semibold">
                  <i className="fas fa-envelope me-1"></i> Email
                </label>
                <input
                  id="email"
                  type="email"
                  className="form-control"
                  placeholder="Enter your email address"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                />
              </div>

              {/* Password Field */}
              <div className="mb-4">
                <label htmlFor="password" className="form-label fw-semibold">
                  <i className="fas fa-lock me-1"></i> Password
                </label>
                <input
                  id="password"
                  type="password"
                  className="form-control"
                  placeholder="Create a strong password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                />
              </div>

              {/* Register Button */}
              <div className="d-grid">
                <button
                  className="btn btn-primary btn-lg fw-bold"
                  onClick={register}
                >
                  <i className="fas fa-user-plus me-2"></i>Register
                </button>
              </div>

              <hr className="my-3" />
              <p className="text-center text-muted mb-0">
                Already have an account?{' '}
                <a href="/djangoapp/login/" className="text-primary fw-semibold">
                  Log in here
                </a>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Register;
