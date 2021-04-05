import logo from './logo.svg';
import './App.css';
import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("http://127.0.0.1:8000/products")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
    return (
        <div class = "services">
          {this.state.data.map(c =>
            <div class="service_item">
              <div class="block_service_img">
              </div>
              <div class="block_service_label">
                <h4>{c.name}</h4>
                <p>{c.description}</p>
              </div>
            </div>
          )}
        </div>
    );
  }
}

export default App;
const container = document.getElementById("root");
render(<App />, container);