import { IfxDatePicker } from '@infineon/infineon-design-system-react';
import './datepicker.scss';

function DatePicker( { error, disabled, size, success, value, max, min, label, caption }) {
  return (
    <IfxDatePicker error={error} disabled={disabled} size={size} success={success} value={value} max={max} min={min} label={label} caption={caption}></IfxDatePicker>
  );
}

export default DatePicker;