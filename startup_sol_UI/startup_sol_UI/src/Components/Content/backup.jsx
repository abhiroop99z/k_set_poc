<Container>
<Card className={styles.customCard}>
  <Card.Title className={styles.title}>{props.title}</Card.Title>
  <a target="_blank" href={`${link}&embedded=true`}>
    <Card.Subtitle className={`mb-2 text-muted ${styles.subTitle}`}>
      {/* {props.link} */}
      <span className={styles.documentLink}>View document</span>
    </Card.Subtitle>
  </a>
  <div className={styles.box}>
    <iFrame src={link} className={styles.preview}></iFrame>
  </div>
  <Card.Body className={styles.customCardBody}>
    {/* <Card.Text className={styles.cardData}>
      <strong>Customer Name :-</strong> {props.customerName}  </Card.Text> */}
    <Card.Text className={styles.cardData}>
      <strong>Service Type :-</strong> {props.serviceType}{" "}
      {/* Path traversal :- Data coming from backend. */}
      {props.path != null ? (
        <p className={styles.traversal}>
          {props.path.map((e, i) => {
            return (
              <>
                {e}{" "}
                {i === props.path.length - 1 ? "" : <BsArrowRight />}{" "}
              </>
            );
          })}
        </p>
      ) : null}
    </Card.Text>

    <Card.Text className={styles.cardData}>
      <strong>Date of Publication :-</strong> {props.publicationDate}
    </Card.Text>
    <Card.Text className={styles.cardData}>
      <strong>Vertical :-</strong> {props.vertical}
    </Card.Text>
  </Card.Body>
</Card>
</Container>

