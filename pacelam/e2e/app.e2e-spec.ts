import { PacelamPage } from './app.po';

describe('pacelam App', () => {
  let page: PacelamPage;

  beforeEach(() => {
    page = new PacelamPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!');
  });
});
