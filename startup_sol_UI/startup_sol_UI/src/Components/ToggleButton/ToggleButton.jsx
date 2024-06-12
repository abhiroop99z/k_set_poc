import React, { Fragment, useContext } from "react";
import Form from "react-bootstrap/Form";

// import "./ToggleButton.css";
import classes from "./ToggleButton.module.css";

import { FetchDataContext } from "../../Context/FetchDataContext";

function CustomToggleButton() {
  const {
    pdfSelectedValue,
    setPdfSelectedValue,
    isResetFilter,
    setIsResetFilter
  } = useContext(FetchDataContext);

  const handlePdfToggle = e => {
    console.log(e);
    if (e.target.checked === true) {
      setPdfSelectedValue(["Yes"]);
    }
    if (e.target.checked === false) {
      setPdfSelectedValue(["No"]);
    }
  };

  return (
    <Fragment>
      {isResetFilter ? (
        <Form.Check
          className={classes.customToggle}
          type="switch"
          id="custom-switch"
          label="Yes"
          value={pdfSelectedValue}
          onChange={handlePdfToggle}
          checked={false}
        ></Form.Check>
      ) : (
        <Form.Check
          className={classes.customToggle}
          type="switch"
          id="custom-switch"
          label="Yes"
          value={pdfSelectedValue}
          onChange={handlePdfToggle}
        ></Form.Check>
      )}
    </Fragment>
  );
}

export default CustomToggleButton;
