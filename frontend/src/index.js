import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import ViewImage from "./ViewImage";
import * as serviceWorker from "./serviceWorker";
import {
	BrowserRouter as Router,
	Switch,
	Route,
	Link,
	useRouteMatch
} from "react-router-dom";

ReactDOM.render(
	<Router>
		<Switch>
			<Route exact path="/">
				<App />
			</Route>
			<Route
				exact
				path="/image/:name"
				render={props => <ViewImage {...props} />}
			/>
			<Route path="/image/:name">
				<ViewImage />
			</Route>
		</Switch>
	</Router>,
	document.getElementById("root")
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
//<Route path="/image/:name">
//				<ViewImage />
//			</Route>
