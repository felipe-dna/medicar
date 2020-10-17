import { Component, OnInit } from '@angular/core';

export interface PeriodicElement {
  name: string;
  position: number;
  weight: number;
  symbol: string;
  userId: string;
}

const ELEMENT_DATA: PeriodicElement[] = [
  {position: 1, name: 'Hydrogen', weight: 1.0079, symbol: 'H', userId: "dpsapodaos"},
  {position: 1, name: 'Hydrogen', weight: 1.0079, symbol: 'H', userId: "dpsapodaos"},
  {position: 1, name: 'Hydrogen', weight: 1.0079, symbol: 'H', userId: "dpsapodaos"},
  {position: 1, name: 'Hydrogen', weight: 1.0079, symbol: 'H', userId: "dpsapodaos"},
  {position: 1, name: 'Hydrogen', weight: 1.0079, symbol: 'H', userId: "dpsapodaos"},
  {position: 1, name: 'Hydrogen', weight: 1.0079, symbol: 'H', userId: "dpsapodaos"},
  {position: 1, name: 'Hydrogen', weight: 1.0079, symbol: 'H', userId: "dpsapodaos"},
  {position: 1, name: 'Hydrogen', weight: 1.0079, symbol: 'H', userId: "dpsapodaos"},
  {position: 1, name: 'Hydrogen', weight: 1.0079, symbol: 'H', userId: "dpsapodaos"},
  {position: 1, name: 'Hydrogen', weight: 1.0079, symbol: 'H', userId: "dpsapodaos"},
  {position: 1, name: 'Hydrogen', weight: 1.0079, symbol: 'H', userId: "dpsapodaos"},
  {position: 1, name: 'Hydrogen', weight: 1.0079, symbol: 'H', userId: "dpsapodaos"},
];


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})

export class HomeComponent {
  displayedColumns: string[] = ['position', 'name', 'weight', 'symbol'];
  dataSource = ELEMENT_DATA;
}
