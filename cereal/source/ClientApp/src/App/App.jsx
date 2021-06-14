import React from 'react';
import { Router, Route, Link } from 'react-router-dom';

import { history } from '../_helpers';
import { authenticationService } from '../_services';
import { PrivateRoute } from '../_components';
import { HomePage } from '../HomePage';
import { LoginPage } from '../LoginPage';
import { AdminPage } from '../AdminPage';

import './App.css';

class App extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            currentUser: null
        };
    }

    componentDidMount() {
        authenticationService.currentUser.subscribe(x => this.setState({ currentUser: x }));
    }

    logout() {
        authenticationService.logout();
        history.push('/login');
    }

    render() {
        const { currentUser } = this.state;
        return (
            <Router history={history}>
                <div className="jumbotron" >
                    <div className="container">
                        <div className="row">
                            <div className="col-md-6 offset-md-3">
                                <PrivateRoute exact path="/" component={HomePage} />
                                <PrivateRoute path="/admin" component={AdminPage} />
                                <Route path="/login" component={LoginPage} />
                            </div>
                        </div>
                    </div>
                </div>
            </Router>
        );
    }
}

export { App }; 