// Import necessary components and functions from react-router-dom.

import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
} from "react-router-dom";
import { Layout } from "./pages/Layout";
import { Home } from "./pages/Home";
import { ErrandDetail } from "./pages/ErrandDetail";
import { MiPerfil } from "./pages/MiPerfil";
import { LoginPage } from "./pages/LoginPage";
import { SignupPage } from "./pages/SignupPage";
import { Favorites } from "./pages/Favorites";
import { FollowUp } from "./pages/FollowUp";
import { ResetPasswordForm } from "./pages/ResetPasswordForm";
import { ForgotPassword } from "./pages/ForgotPassword";

export const router = createBrowserRouter(
  createRoutesFromElements(
    // CreateRoutesFromElements function allows you to build route elements declaratively.
    // Create your routes here, if you want to keep the Navbar and Footer in all views, add your new routes inside the containing Route.
    // Root, on the contrary, create a sister Route, if you have doubts, try it!
    // Note: keep in mind that errorElement will be the default page when you don't get a route, customize that page to make your project more attractive.
    // Note: The child paths of the Layout element replace the Outlet component with the elements contained in the "element" attribute of these child paths.

    // Root Route: All navigation will start from here.
    <Route path="/" element={<Layout />} errorElement={<h1>Not found!</h1>} >

      {/* Nested Routes: Defines sub-routes within the BaseHome component. */}
      <Route path="/" element={<Home />} />
      <Route path="/signup" element={<SignupPage />} />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/user_profile" element={<MiPerfil />} />
      <Route path="/errands/:errand_id" element={<ErrandDetail />} />
      <Route path="/favorites" element={<Favorites />} />
      <Route path="/follow_up" element={<FollowUp />} />
      <Route path="/reset-password" element={<ResetPasswordForm />} />
      <Route path="/forgot-password" element={<ForgotPassword />} />
    </Route>
  )
);