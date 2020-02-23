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
	useRouteMatch
} from "react-router-dom";

class App extends React.Component {
	constructor(props) {
		super(props);
		const initialImg = [];

		this.state = {
			images: initialImg,
			selectedFile: "",
			selectedName: "",
			selectedMessage: ""
		};

		this.onClickHandle = this.onClickHandle.bind(this);
		this.onChangeName = this.onChangeName.bind(this);
		this.onChangeHandle = this.onChangeHandle.bind(this);
		this.getAll = this.getAll.bind(this);
	}
	componentDidMount() {
		this.getAll();
	}
	getAll() {
		axios.get("http://localhost:8081/images").then(response => {
			const images = [];

			response.data.images.forEach(element => {
				images.push({
					path: element.path,
					name: element.name
				});
			});
			this.setState({ images: images });
		});
	}
	onClickHandle(e) {
		if (this.state.selectedName === "") {
			this.setState({
				selectedMessage: "please select one name"
			});
			return;
		} else if (this.state.selectedFile === "") {
			this.setState({
				selectedMessage: "please select one image"
			});
			return;
		}
		const data = new FormData();
		data.append("name", this.state.selectedName);
		data.append("file", this.state.selectedFile);
		axios.post("http://localhost:8081/images", data, {})
			.then(res => {
				if (res.data.status === "CREATED") {
					this.setState({
						selectedMessage: `${this.state.selectedName} image uploaded`
					});
				} else if (res.data.status === "UPDATED") {
					this.setState({
						selectedMessage: `${this.state.selectedName} image changed`
					});
				} else {
					//something wrong!
				}

				this.getAll();
			})
			.catch(error => {
				this.setState({
					selectedMessage: error.response.data
				});
			});
	}
	onChangeName(e) {
		this.setState({
			selectedName: e.target.value
		});
	}
	onChangeHandle(e) {
		this.setState({
			selectedFile: e.target.files[0]
		});
	}
	render() {
		return (
			<div className="App">
				<header>
					<div>
						<span>
							{
								this.state
									.selectedMessage
							}
						</span>
					</div>
					<input
						type="text"
						name="name"
						onChange={this.onChangeName}
					/>
					<input
						type="file"
						name="file"
						onChange={this.onChangeHandle}
					/>
					<button
						type="button"
						onClick={this.onClickHandle}
					>
						Upload
					</button>
					{this.state.images.map(
						(element, idx) => {
							return (
								<div key={idx}>
									<Row
										style={{
											display:
												"inline-flex",
											alignItems:
												"center"
										}}
									>
										<Col>
											<img
												src={
													element.path
												}
												style={{
													heigth:
														"150px",
													width:
														"150px"
												}}
											/>
										</Col>
										<Col>
											<Link
												to={`/image/${element.name}`}
											>
												{
													element.name
												}
											</Link>
										</Col>
									</Row>
								</div>
							);
						}
					)}
				</header>
			</div>
		);
	}
}

export default App;
