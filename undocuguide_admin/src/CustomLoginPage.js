import React from 'react';
import { useLogin, useNotify, useTranslate, Notification } from 'react-admin';
import { Button } from '@mui/material';
import { makeStyles } from '@mui/styles';
import { googleProvider } from './firebase';

const useStyles = makeStyles({
  loginButton: {
    marginTop: '1em',
  },
});

const CustomLoginPage = () => {
  const login = useLogin();
  const notify = useNotify();
  const translate = useTranslate();
  const classes = useStyles();

  const signInWithGoogle = () => {
    login({ provider: googleProvider })
      .catch((error) => {
        notify(translate('ra.message.error'), 'warning');
      });
  };

  return (
    <div>
      <Button
        variant="contained"
        color="primary"
        className={classes.loginButton}
        onClick={signInWithGoogle}
      >
        Sign in with Google
      </Button>
      <Notification />
    </div>
  );
};

export default CustomLoginPage;
