import React from 'react';
import { Formik, Field, Form, ErrorMessage } from 'formik';
import { ChromePicker  } from 'react-color';
import * as Yup from 'yup';

import { requestService } from '../_services';


const SketchPickerField = ({ name, value, onChange }) => {
    return (
        <ChromePicker
            color={value}
            onChange={val => {
                onChange(name, val.hex);
            }}
        />
    );
};

class HomePage extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
        };
    }
    
    render() {
        return (
            <div>
                <h2>Cereal Request</h2>
                <Formik
                    initialValues={{
                        title: '',
                        flavor: '',
                        color: '#FFF',
                        description: ''
                    }}
                    validationSchema={Yup.object().shape({
                        title: Yup.string().required('Title is required'),
                        flavor: Yup.string().required('Flavor is required'),
                        color: Yup.string().required('Color is required'),
                        description: Yup.string().required('Description is required')
                    })}
                    onSubmit={({ title, flavor, color, description }, { setStatus, setSubmitting }) => {
                        setStatus();
                        requestService.requestCereal(JSON.stringify({ title, flavor, color, description }))
                            .then(
                                resp => {
                                    setSubmitting(false);
                                    setStatus({ 'type': 'success', 'message': resp.message });
                                },
                                error => {
                                    setSubmitting(false);
                                    setStatus({ 'type': 'error', 'message': error });
                                }
                            );
                    }}
                    render={({ errors, status, touched, values, isSubmitting, setFieldValue }) => (
                        <Form>
                            <div className="form-group">
                                <label htmlFor="title">Title</label>
                                <Field name="title" type="text" className={'form-control' + (errors.title && touched.title ? ' is-invalid' : '')} />
                                <ErrorMessage name="title" component="div" className="invalid-feedback" />
                            </div>
                            <div className="form-group">
                                <label htmlFor="flavor">Flavor</label>
                                <Field as="select" name="flavor" className={'form-control' + (errors.flavor && touched.flavor ? ' is-invalid' : '')}>
                                    <option value="" label="Select your flavor!" />
                                    <option value="bacon">🥓</option>
                                    <option value="pizza">🍕</option>
                                    <option value="broccoli">🥦</option>
                                    <option value="donut">🍩</option>
                                    <option value="sushi">🍣</option>
                                    <option value="taco">🌮</option>
                                    <option value="meat">🍗</option>
                                    <option value="grape">🍇</option>
                                    <option value="corn">🌽</option>
                                    <option value="smokin">🌶️</option>
                                </Field>
                                <ErrorMessage name="flavor" component="div" className="invalid-feedback" />
                            </div>
                            <div className="form-group">
                                <label htmlFor="color">Color</label>
                                <SketchPickerField
                                    name="color"
                                    value={values.color}
                                    onChange={setFieldValue}
                                />
                                <ErrorMessage name="color" component="div" className="invalid-feedback" />
                            </div>
                            <div className="form-group">
                                <label htmlFor="description">Description</label>
                                <Field name="description" type="text" className={'form-control' + (errors.description && touched.description ? ' is-invalid' : '')} />
                                <ErrorMessage name="description" component="div" className="invalid-feedback" />
                            </div>
                            <div className="form-group">
                                <button type="submit" className="btn btn-secondary" disabled={isSubmitting}>Request</button>
                                {isSubmitting &&
                                    <img src="data:image/gif;base64,R0lGODlhEAAQAPIAAP///wAAAMLCwkJCQgAAAGJiYoKCgpKSkiH/C05FVFNDQVBFMi4wAwEAAAAh/hpDcmVhdGVkIHdpdGggYWpheGxvYWQuaW5mbwAh+QQJCgAAACwAAAAAEAAQAAADMwi63P4wyklrE2MIOggZnAdOmGYJRbExwroUmcG2LmDEwnHQLVsYOd2mBzkYDAdKa+dIAAAh+QQJCgAAACwAAAAAEAAQAAADNAi63P5OjCEgG4QMu7DmikRxQlFUYDEZIGBMRVsaqHwctXXf7WEYB4Ag1xjihkMZsiUkKhIAIfkECQoAAAAsAAAAABAAEAAAAzYIujIjK8pByJDMlFYvBoVjHA70GU7xSUJhmKtwHPAKzLO9HMaoKwJZ7Rf8AYPDDzKpZBqfvwQAIfkECQoAAAAsAAAAABAAEAAAAzMIumIlK8oyhpHsnFZfhYumCYUhDAQxRIdhHBGqRoKw0R8DYlJd8z0fMDgsGo/IpHI5TAAAIfkECQoAAAAsAAAAABAAEAAAAzIIunInK0rnZBTwGPNMgQwmdsNgXGJUlIWEuR5oWUIpz8pAEAMe6TwfwyYsGo/IpFKSAAAh+QQJCgAAACwAAAAAEAAQAAADMwi6IMKQORfjdOe82p4wGccc4CEuQradylesojEMBgsUc2G7sDX3lQGBMLAJibufbSlKAAAh+QQJCgAAACwAAAAAEAAQAAADMgi63P7wCRHZnFVdmgHu2nFwlWCI3WGc3TSWhUFGxTAUkGCbtgENBMJAEJsxgMLWzpEAACH5BAkKAAAALAAAAAAQABAAAAMyCLrc/jDKSatlQtScKdceCAjDII7HcQ4EMTCpyrCuUBjCYRgHVtqlAiB1YhiCnlsRkAAAOwAAAAAAAAAAAA==" />
                                }
                            </div>
                            {status &&
                                <div className={'alert' + (status.type == 'error' ? ' alert-danger' : ' alert-success')}>{status.message}</div>
                            }
                        </Form>
                    )}
                />
            </div>
        )
    }
}

export { HomePage };