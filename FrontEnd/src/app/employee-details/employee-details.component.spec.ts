import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EmployeeDetailsComponent } from './employee-details.component';
import { RouterModule } from '@angular/router';

describe('EmployeeDetailsComponent', () => {
  let component: EmployeeDetailsComponent;
  let fixture: ComponentFixture<EmployeeDetailsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EmployeeDetailsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EmployeeDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
