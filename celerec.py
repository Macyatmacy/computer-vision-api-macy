#!/usr/bin/env python3

import boto3
import click

@click.command(help="This tool does celebrity detection")
@click.option('--file', default="queen.jpg", prompt='I need the name of the file in the bucket',
              help='This is the name of the file in the bucket')


def recognize_celebrities(file):
    client=boto3.client('rekognition')

    response = client.recognize_celebrities(
        Image={
            'S3Object': {
                'Bucket': 'cvapimacy',
                'Name': file,
            },
        },
    )
    
    click.echo(click.style(f"Detecting Celebrities for: {file}", fg="red"))
    
    for celebrity in response['CelebrityFaces']:
        print ('Name: ' + celebrity['Name'])
        print ('Id: ' + celebrity['Id'])
        print ('Position:')
        print ('   Left: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Height']))
        print ('   Top: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Top']))
        print ('Info')
        for url in celebrity['Urls']:
            print ('   ' + url)
        return celebrity['Name']

if __name__ == '__main__':
    # pylint: disable=E1120
    recognize_celebrities()
