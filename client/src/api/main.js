export default function (cli) {
  return {
    eventList(){
      return cli.get('api/events/')
    }
  }
}
