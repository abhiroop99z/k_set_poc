import React, { useState } from "react";
import Container from "react-bootstrap/Container";
import styles from "./Contents.module.css";
import Card from "react-bootstrap/Card";
// import { FetchDataContext } from "../../Context/FetchDataContext";

import { BsArrowRight } from "react-icons/bs";

function Content(props) {
  // const { getData } = useContext(FetchDataContext);

  const [isShowText, setIsShowText] = useState(true);

  const link = "https://en.wikipedia.org/wiki/Zensar_Technologies";

  const toggleReadMore = () => {
    setIsShowText(!isShowText);
  };

  // var pathList = [];
  // const path = "";
  {
    // When actual data will come from backend use this.
    // getData != null ? (pathList = props.path) : (pathList = null);
  }
  console.log(props.technologyFocus);
  return (
    <div className={styles.customContainer}>
      <div>
        {/*  Only for testing of dynamic data render. Can delete it later on. */}

        {/* companyName={data.companyName}
      city={data.city}
      state={data.state}
      country={data.country}
      technologyFocus={data.technologyFocus}
      engagementDetails={data.engagementDetails}
      vertical={data.vertical}
      activeCustomers={data.activeCustomers}
      usecase={data.usecase}
      feedback={data.feedback}
      zensarCustomers={data.zensarCustomers} */}

        {/* <Container className={styles.customCard}> */}
        <Card className={styles.customCard}>
          <Card.Title className={styles.title}>{props.companyName}</Card.Title>
          <Card.Body className={styles.customCardBody}>
            {/* {
              // console.log(props.company)
              props.company!==null && 
              Object.entries(props.company).map(([k, v], index) => {
                return (<Card.Text className={styles.cardData}>
                  <strong>{k} :-</strong> {v}{" "}
                </Card.Text>

                )
              })
            } */}

            {/* {props.city !== "" && (
              <Card.Text className={styles.cardData}>
                <strong>Company :-</strong> {props.city}{" "}
              </Card.Text>
            )} */}
            {props.city !== "" && (
              <Card.Text className={styles.cardData}>
                <strong>City :-</strong> {props.city}{" "}
              </Card.Text>
            )}
            {props.state !== "" && (
              <Card.Text className={styles.cardData}>
                <strong>State :-</strong> {props.state}{" "}
              </Card.Text>
            )}

            {props.country !== "" && (
              <Card.Text className={styles.cardData}>
                <strong>Country :-</strong> {props.country}
              </Card.Text>
            )}
            {props.technologyFocus !== "" && (
              <Card.Text className={styles.cardData}>
                <strong>Technology Focus :-</strong> {props.technologyFocus}
              </Card.Text>
            )}
            {props.engagementDetails !== "" && (
              <Card.Text className={styles.cardData}>
                <strong>Engagement Details :-</strong> {props.engagementDetails}
              </Card.Text>
            )}
            {props.vertical !== "" && (
              <Card.Text className={styles.cardData}>
                <strong>Vertical :-</strong> {props.vertical}
              </Card.Text>
            )}
            {props.activeCustomers !== "" && (
              <Card.Text className={styles.cardData}>
                <strong>Active Customers :-</strong> {props.activeCustomers}
              </Card.Text>
            )}
            {props.usecase !== "" && (
              <Card.Text className={styles.cardData}>
                <strong>Usecase :-</strong>
                {props.usecase}
              </Card.Text>
            )}
            {props.venture !== "" && (
              <Card.Text className={styles.cardData}>
                <strong>Venture :-</strong>
                {props.venture}
              </Card.Text>
            )}
            {props.zensarCustomers !== "" && (
              <Card.Text className={styles.cardData}>
                <strong>Zensar Customers :-</strong>
                {props.zensarCustomers}
              </Card.Text>
            )} 
          </Card.Body>
        </Card>
        {/* </Container> */}
      </div>
    </div>
  );
}

export default Content;
