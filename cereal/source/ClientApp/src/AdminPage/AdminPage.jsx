import React from 'react';
import { MarkdownPreview } from 'react-marked-markdown';
import { requestService, authenticationService } from '../_services';
import { Accordion, Card, Button } from 'react-bootstrap'

class RequestCard extends React.Component {
    componentDidCatch(error) {
        console.log(error);
    }

    render() {
        try {
            let requestData;
            try {
                requestData = JSON.parse(this.props.request.json);
            } catch (e) {
                requestData = null;
            }
            return (
                <Card>
                    <Card.Header>
                        <Accordion.Toggle as={Button} variant="link" eventKey={this.props.request.requestId} name="expand" id={this.props.request.requestId}>
                            {requestData && requestData.title && typeof requestData.title == 'string' && 
                                <MarkdownPreview markedOptions={{ sanitize: true }} value={requestData.title} />
                            }
                        </Accordion.Toggle>
                    </Card.Header>
                    <Accordion.Collapse eventKey={this.props.request.requestId}>
                        <div>
                            {requestData &&
                                <Card.Body>
                                    Description:{requestData.description}
                                    <br />
                                    Color:{requestData.color}
                                    <br />
                                    Flavor:{requestData.flavor}
                                </Card.Body>
                            }
                        </div>
                    </Accordion.Collapse>
                </Card>
            );
        } catch (e) { console.log(e); return null };
    }
}

class AdminPage extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            requests: null,
        };
    }

    componentDidMount() {
        requestService.getCerealRequests().then(requests => this.setState({ requests }));
    }

    render() {
        const { requests } = this.state;
        return (
            <div className="card card-body bg-light">
                <h3>Current cereal requests:</h3>
                {requests &&
                    <Accordion>
                    {requests.map(request =>
                        <>
                            <RequestCard request={request}/>
                            <br />
                        </>
                    )}
                    </Accordion>
                }
            </div>
        );
    }
}

export { AdminPage };