import React from 'react';
import { Route, Switch } from 'react-router-dom';

import PageNotFound from './PageNotFound';
import Header from './common/Header';
import ProfilePage from './core/ProfilePage';
import PrivateRoute from './authentication/PrivateRoute';
import LoginPage from './authentication/LoginPage';
import SignUpPage from './authentication/SignUpPage';

import Dashboard from './core/Dashboard';
import Teams from './core/Teams';

function App() {
	return (
		<React.Fragment>
			{/* <Header /> */}
			<Switch>
				{/* <PrivateRoute exact path="/profile" component={ProfilePage} />
				<Route path="/login" component={LoginPage} />
				<Route path="/sign-up" component={SignUpPage} />
				<Route component={PageNotFound} /> */}
				<Route exact path="/" component={Dashboard} />
				<Route path="/teams" component={Teams} />
			</Switch>
		</React.Fragment>
	);
}
export default App;
