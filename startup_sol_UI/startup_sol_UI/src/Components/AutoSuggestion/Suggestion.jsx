import React from "react";
import styles from "./Suggestion.module.css";

function Suggestion(props) {
  console.log(props);
  return (
    <div>
      {/*  Show if no suggestion available  */}

      {/* {Object.entries(isSuggestion).length == 0 && searchQuery !== "" && (
                <Card className="suggestionClass">
                  <p className="noKey">No suggestions available</p>
                </Card>
              )} */}

      {/* Show if suggestions are available */}
      {/* Auto suggestion based on user input */}
      {Object.entries(isSuggestion).length !== 0 && searchQuery !== "" && (
        <Card className="suggestionClass">
          {/* {isSuggestion.length !== 0 &&
                  // searchTarget === "" && */}
          {Object.entries(isSuggestion).map(([key, value]) => {
            // console.log(key);
            return value.map(e => {
              return (
                <ListGroup
                  onClick={() => suggestHandler(key)}
                  className="suggestionClassList"
                >
                  <ListGroup.Item className="ListGroup">
                    <p className={"key"}>{key}</p>
                    <p className="cardValue">{e}</p>
                  </ListGroup.Item>
                </ListGroup>
              );
            });
          })
          // })
          }
        </Card>
      )}

      {/* Backup */}
      {/* {isSuggestion.length !== 0 &&
                searchTarget === "" &&
                Object.entries(isSuggestion).map(([key, value]) =>
                  // console.log({key} , {value}
                  // value.map(e => {
                  {
                    return (
                      <Card className="suggestionClass">
                        {value.map(e => {
                          <ListGroup onClick={() => suggestHandler(key)}>
                            <ListGroup.Item className={"key"}>
                              {key} {e}
                            </ListGroup.Item>
                          </ListGroup>;
                        })}
                      </Card>
                    );
                    // })
                  }
                )} */}
    </div>
  );
}

export default Suggestion;
