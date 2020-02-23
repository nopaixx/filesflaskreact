import React, { useState, useEffect } from "react";
import { Container, Row, Col } from "reactstrap";
import logo from "./logo.svg";
import "./App.css";
import axios from "axios";
import {
	BrowserRouter as Router,
	Switch,
	Route,
	Link,
	useRouteMatch,
	useParams
} from "react-router-dom";

class ViewImage extends React.Component {
	constructor(props) {
		super(props);
		this.getImage = this.getImage.bind(this);
		this.state = { image: { src: "", title: "" } };
		console.log(this.props);
		//		const { name } = useParams();
		//		this.getImage(name);
	}
	getImage(name) {
		axios.get(`http://localhost:8081/images/${name}`).then(
			response => {
				console.log(response);
				if (response.status === 200) {
					this.setState({
						image: {
							src:
								response.data
									.image
									.path,
							title:
								response.data
									.image
									.name
						}
					});
				} else {
					// something wrong...
				}
			}
		);
	}
	render() {
		return (
			<div className="App">
				<Row>
					<Col>
						{this.state.image.title !== ""
							? this.state.image.title
							: ""}
					</Col>
					<Col>
						{this.state.image.src !== "" ? (
							<img
								src={
									this
										.state
										.image
										.src
								}
							/>
						) : (
							""
						)}
					</Col>
				</Row>
			</div>
		);
	}
}

export default ViewImage;
