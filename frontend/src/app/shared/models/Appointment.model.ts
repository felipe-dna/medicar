export class Speciality {
  id: string;
  name: string;
}

export class Doctor {
  id: string;
  name: string;
  speciality: Speciality;
}

export class Appointment {
  id: string;
  time: string;
}

export class AvailableTime {
  id: string;
  day: string;
  time: string;
  Doctor: string;
  Patient: string;
}

export class Schedule {
  id: string;
  doctor: string;
  day: string;
  // tslint:disable-next-line:variable-name
  available_times: AvailableTime[];
}
