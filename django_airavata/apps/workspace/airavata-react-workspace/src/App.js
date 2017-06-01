import React, { Component } from 'react';

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {'projects': []};
        fetch('/api/projects',{
            credentials: 'include'
        }).then((response) => {
            return response.json();
        }).then((projects) => {
            this.setState({'projects': projects});
        });
    }
    render() {
        console.log("this.state.projects", this.state.projects);
        const projects = this.state.projects.map((project) =>
            <li key={project.projectID}>{project.name}</li>
        );
        return (
            <div className="App">
                <ul>
                    {projects}
                </ul>
            </div>
        );
    }
}

export default App;
