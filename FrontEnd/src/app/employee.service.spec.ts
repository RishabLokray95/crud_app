import { TestBed, inject, async } from '@angular/core/testing';

import { EmployeeService } from './employee.service';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';




describe('EmployeeService', () => {
  let employeeservice: EmployeeService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [
        HttpClientTestingModule,
      ],
      providers: [
        EmployeeService
      ],

    });

    employeeservice = TestBed.get(EmployeeService);
    httpMock = TestBed.get(HttpTestingController);
  });

  it('should be created', () => {
    expect(employeeservice).toBeTruthy();
  });


  it(`should fetch posts as an Observable`, async(inject([HttpTestingController, EmployeeService],
    (httpClient: HttpTestingController, postService: EmployeeService) => {

      const postItem = [
        {
          "id": 1,
          "name": "Rishab",
          "email": "rishab@gmail.com",
          "number":123
        }
      ];


      postService.getEmployeesList()
        .subscribe((posts: any) => {
          expect(posts.length).toBe(1);
        });

      let req = httpMock.expectOne('http://localhost:8000/posts');
      expect(req.request.method).toBe("GET");

      req.flush(postItem);
      httpMock.verify();

    })));



});



