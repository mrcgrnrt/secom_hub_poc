import { useEffect } from 'react';
import { IfxStepper, IfxStep } from '@infineon/infineon-design-system-react';
import './stepper.scss';

function Stepper( { activeStep, showStepNumber, variant }) {

  useEffect(() => {
    const mediaQueryList = window.matchMedia('(max-width: 768px)');

    const handleMediaQueryChange = (event) => {
      const matches = event ? event.matches : mediaQueryList.matches;
      if (matches) {
        /* The viewport is 800px wide or less */
        toggleVariant('compact');
      } else { 
        /* The viewport is more than 800px wide */
        toggleVariant('default');
      }
    };

    mediaQueryList.addEventListener('change', handleMediaQueryChange);
    return () => {
      mediaQueryList.removeEventListener('change', handleMediaQueryChange);
    };
  }, []);

  const toggleVariant = (variant) => { 
    const stepper = document.querySelector('ifx-stepper');
    if(variant === 'default') { 
      stepper.variant = 'default';
    } else if(variant === 'compact') { 
      stepper.variant = 'compact';
    }
  }

  return (
    <IfxStepper active-step={activeStep} show-step-number={showStepNumber} variant={variant}>
      <IfxStep>Step Label 1</IfxStep>
      <IfxStep>Step Label 2</IfxStep>
      <IfxStep>Step Label 3</IfxStep>
    </IfxStepper>
  );
}

export default Stepper;