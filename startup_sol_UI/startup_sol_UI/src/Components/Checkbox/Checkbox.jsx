import React, { useContext, Fragment } from "react";
import classes from "./Checkbox.module.css";
import { FetchDataContext } from "../../Context/FetchDataContext";
import Form from "react-bootstrap/Form";

function CheckBoxFilter(props) {
  const {
    dataFromAPI,
    isResetFilter,
    masterSelected,
    setMasterSelected,
    isCheckValue,
    setIsCheckValue
  } = useContext(FetchDataContext);

  // Custom handler functions starts.

  const masterOnChangeHandler = event => {
    var { value, type, checked } = event.target;
    const newValue = type === "cehckbox" ? checked : value;
    // const newValue = value;
    let newArray = [...isCheckValue, newValue];
    if (isCheckValue.includes(event.target.value)) {
      newArray = newArray.filter(v => v !== event.target.value);
    }
    setIsCheckValue(newArray);

    if (masterSelected.length === 0) {
      setMasterSelected(prev => [{ ...prev, [props.name]: [newValue] }]);
    } else {
      masterSelected.map((e, i) => {
        if (e.hasOwnProperty(props.name)) {
          Object.keys(e).map(k => {
            if (e[k].includes(newValue)) {
              e[k].pop(newValue);
            } else {
              e[k].push(newValue);
            }
          });
          setMasterSelected(masterSelected);
        } else {
          let newArray = [...masterSelected, { [props.name]: [newValue] }];
          setMasterSelected(newArray);
        }
      });
    }
  };

  // Custom handler functions ends.

  var data = dataFromAPI["filters"];

  return (
    <div>
      {data.map((e, i) => {
        return (
          <Fragment>
            {e.ui_name === props.uiName && props.active && e.ui_name == props.value
              ? e.type_of_value.map((f, j) => {
                  return (
                    <div>
                      {/* If reset filter is clicked and no filters or checkboxes are selected make checked false and show the below div. */}
                      {isResetFilter ? (
                        <Form.Check
                          className={classes.customCheckbox}
                          type="checkbox"
                          label={f}
                          value={f}
                          checked={false}
                          onChange={masterOnChangeHandler}
                          disabled={e.type_of_value.length == 1}
                        />
                      ) : (
                        // If filter is applied and checkboxes are selected make checked true for the respective filter and show the below div.
                        <Form.Check
                          className={classes.customCheckbox}
                          type="checkbox"
                          label={f}
                          value={f}
                          checked={isCheckValue.includes(f) ? true : false}
                          onChange={masterOnChangeHandler}
                          disabled={e.type_of_value.length == 1}
                        />
                      )}
                    </div>
                  );
                })
              : null}
          </Fragment>
        );
      })}
    </div>
  );
}

export default CheckBoxFilter;
