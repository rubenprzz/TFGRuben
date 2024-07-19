import React, { Component } from "react";
import CreateEstudiantePage from "./CreateEstudiantePage";
import { Link } from "react-router-dom"; // Optional: For navigation

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
        <div>
          <p>This is the home page</p>
          <Link to="/api/createEstudiante">Create Estudiante</Link> {/* Optional: For navigation */}
          <p>Pepe</p>

        </div>
    );
  }
}
